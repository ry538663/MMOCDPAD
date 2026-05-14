document.addEventListener('DOMContentLoaded', () => {
    const simulateBtn = document.getElementById('simulate-btn');
    const aiFeed = document.getElementById('ai-decision-feed');
    const networkGraph = document.getElementById('network-graph');
    
    // SocketIO Initialization
    const socket = io();

    socket.on('new_packet', (data) => {
        console.log('Live packet received:', data);
        addAIDecision(data);
        updateStats();
        updateLogs();
        animatePacket(data.device_id);
        showToast(`Security Alert: Packet ${data.action} for ${data.device_id}`, data.action === 'Allowed' ? 'success' : 'danger');
    });

    // Initial Stats Load
    updateStats();
    updateLogs();
    initNetworkGraph();

    simulateBtn.addEventListener('click', async () => {
        simulateBtn.disabled = true;
        simulateBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Processing...';
        
        try {
            const response = await fetch('/api/simulate_packet');
            const data = await response.json();
            
            addAIDecision(data);
            updateStats();
            updateLogs();
            animatePacket(data.device_id);
            
        } catch (error) {
            console.error('Simulation error:', error);
        } finally {
            simulateBtn.disabled = false;
            simulateBtn.innerHTML = '<i class="fas fa-plus-circle me-2"></i> Simulate Packet';
        }
    });

    async function updateStats() {
        const res = await fetch('/api/stats');
        const data = await res.json();
        document.getElementById('total-devices').innerText = data.total_devices;
        document.getElementById('anomalies-blocked').innerText = data.anomalies_detected;
        document.getElementById('avg_trust').innerText = data.avg_trust_score.toFixed(2);
    }

    async function updateLogs() {
        const res = await fetch('/api/logs');
        const data = await res.json();
        const tbody = document.getElementById('logs-table-body');
        tbody.innerHTML = data.map(log => `
            <tr>
                <td>${log.timestamp}</td>
                <td>${log.device_id}</td>
                <td><span class="status-badge ${log.action === 'Allow' ? 'status-allowed' : 'status-denied'}">${log.action}</span></td>
                <td>${log.reason}</td>
            </tr>
        `).join('');
    }

    function addAIDecision(data) {
        if (aiFeed.querySelector('.text-muted')) aiFeed.innerHTML = '';
        
        const card = document.createElement('div');
        card.className = `glass-card p-3 mb-3 border-start border-4 ${data.action === 'Allowed' ? 'border-success' : 'border-danger'}`;
        card.innerHTML = `
            <div class="d-flex justify-content-between mb-2">
                <span class="fw-bold">${data.device_id}</span>
                <small class="text-muted">${data.timestamp}</small>
            </div>
            <div class="mb-2" style="font-size: 0.85rem;">
                <div>Proto: <span class="text-info">${data.protocol}</span> | Size: <span class="text-info">${data.packet_size}B</span></div>
                <div>Trust: <span class="text-${data.trust_score > 0.7 ? 'success' : 'warning'}">${(data.trust_score * 100).toFixed(1)}%</span></div>
            </div>
            <div class="d-flex justify-content-between align-items-center mt-2 pt-2 border-top border-secondary">
                <span class="badge ${data.action === 'Allowed' ? 'bg-success' : 'bg-danger'}">${data.action}</span>
                <span class="text-muted" style="font-size: 0.7rem;">HASH: ${data.hash.substring(0, 10)}...</span>
            </div>
        `;
        aiFeed.prepend(card);
    }

    function initNetworkGraph() {
        networkGraph.innerHTML = '';
        // Central Node (ZTS Controller)
        const center = document.createElement('div');
        center.className = 'node animate-pulse';
        center.style.left = '50%';
        center.style.top = '50%';
        center.style.transform = 'translate(-50%, -50%)';
        center.style.background = 'var(--secondary-color)';
        center.style.width = '24px';
        center.style.height = '24px';
        center.id = 'node-center';
        networkGraph.appendChild(center);

        // Device Nodes
        for (let i = 0; i < 5; i++) {
            const angle = (i / 5) * 2 * Math.PI;
            const x = 50 + 35 * Math.cos(angle);
            const y = 50 + 35 * Math.sin(angle);
            
            const node = document.createElement('div');
            node.className = 'node';
            node.style.left = `${x}%`;
            node.style.top = `${y}%`;
            node.id = `node-IIoT_DEV_10${i}`;
            networkGraph.appendChild(node);
            
            // Link
            const link = document.createElement('div');
            link.className = 'link';
            link.style.left = '50%';
            link.style.top = '50%';
            link.style.width = '35%';
            link.style.transform = `rotate(${angle}rad)`;
            networkGraph.appendChild(link);
        }
    }

    function animatePacket(devId) {
        const node = document.getElementById(`node-${devId}`);
        if (!node) return;
        
        const originalShadow = node.style.boxShadow;
        node.style.boxShadow = '0 0 30px #ffffff';
        node.style.transform = 'scale(1.5)';
        
        setTimeout(() => {
            node.style.boxShadow = originalShadow;
            node.style.transform = 'scale(1)';
        }, 500);
    }

    // Helper: Show Notification Toast
    function showToast(message, type) {
        const toast = document.createElement('div');
        toast.className = `glass-card p-3 position-fixed top-0 end-0 m-4 border-start border-4 border-${type} animate-pulse`;
        toast.style.zIndex = '9999';
        toast.innerHTML = `<i class="fas ${type === 'success' ? 'fa-check-circle text-success' : 'fa-exclamation-triangle text-danger'} me-2"></i> ${message}`;
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 4000);
    }
});

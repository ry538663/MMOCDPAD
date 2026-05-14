async function loadCharts() {
    try {
        const response = await fetch('/api/analytics_data');
        const data = await response.json();

        const chartConfig = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: '#cbd5e1', font: { family: 'Outfit' } } }
            },
            scales: {
                x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#cbd5e1' } },
                y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#cbd5e1' } }
            }
        };

        // 1. False Positive Rate Analysis
        new Chart(document.getElementById('fpr-chart'), {
            type: 'line',
            data: {
                labels: ['100', '200', '300', '400', 'Latest'],
                datasets: [{
                    label: 'MMOCDPAD-DRL (Real Data)',
                    data: data.fpr,
                    borderColor: '#00d2ff',
                    tension: 0.4
                }]
            },
            options: chartConfig
        });

        // 2. Data Confidentiality Rate
        new Chart(document.getElementById('confidentiality-chart'), {
            type: 'bar',
            data: {
                labels: ['Baseline', 'AES-128', 'MMO-SPN (Active)'],
                datasets: [{
                    label: 'Confidentiality %',
                    data: data.confidentiality,
                    backgroundColor: ['#3a7bd5', '#1e293b', '#00d2ff'],
                    borderRadius: 8
                }]
            },
            options: chartConfig
        });

        // 3. Data Integrity Rate Analysis
        new Chart(document.getElementById('integrity-chart'), {
            type: 'line',
            data: {
                labels: ['T1', 'T2', 'T3', 'T4', 'T5'],
                datasets: [{
                    label: 'Integrity Rate',
                    data: data.integrity,
                    borderColor: '#22c55e',
                    backgroundColor: 'rgba(34, 197, 94, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: chartConfig
        });

        // 4. Network Access Time Analysis
        new Chart(document.getElementById('access-time-chart'), {
            type: 'bar',
            data: {
                labels: ['Auth', 'Profile Gen', 'DRL Decision', 'Total'],
                datasets: [{
                    label: 'Latency (ms)',
                    data: data.access_time,
                    backgroundColor: '#f59e0b',
                    borderRadius: 8
                }]
            },
            options: chartConfig
        });

    } catch (e) {
        console.error("Error loading analytics data:", e);
    }
}

document.addEventListener('DOMContentLoaded', loadCharts);

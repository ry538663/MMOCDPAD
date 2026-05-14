from scapy.all import sniff, IP, TCP, UDP
import time

class LivePacketCapture:
    """
    Scapy-based live packet listener.
    Extracts metadata for the MMOCDPAD-DRL pipeline.
    """
    def __init__(self, callback=None):
        self.callback = callback
        self.is_running = False

    def packet_handler(self, pkt):
        if IP in pkt:
            proto = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "Other"
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            size = len(pkt)
            
            packet_info = {
                'src_ip': src_ip,
                'dst_ip': dst_ip,
                'protocol': proto,
                'packet_size': size,
                'timestamp': time.strftime('%H:%M:%S')
            }
            
            if self.callback:
                self.callback(packet_info)

    def start_capture(self, interface=None, count=0):
        print(f"Starting live capture on {interface if interface else 'default interface'}...")
        self.is_running = True
        try:
            sniff(iface=interface, prn=self.packet_handler, count=count, store=0)
        except Exception as e:
            print(f"Capture Error: {e}")
            self.is_running = False

if __name__ == "__main__":
    def my_callback(info):
        print(f"Captured: {info}")
    
    cap = LivePacketCapture(callback=my_callback)
    # Note: Requires root/admin privileges on most systems
    print("Press Ctrl+C to stop (Requires sudo on Linux/Mac)")
    cap.start_capture(count=5)

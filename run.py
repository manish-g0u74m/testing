from app import create_app
import socket

app = create_app()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    ip = get_ip()
    print(f"\n===== Restaurant Recommendation System =====")
    print(f"Local network URL: http://{ip}:5000")
    print("- Anyone on your WiFi network can use this URL")
    print("===========================================\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
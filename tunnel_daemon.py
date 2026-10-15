import subprocess
import time
import re
import os
import shutil
import qrcode

tunnel_log_file = r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\current_tunnel.txt'
artifact_dir = r'C:\Users\pcvis\.gemini\antigravity\brain\a19a9203-d8a0-4146-a6aa-7e2a3b778477'

while True:
    print('Starting SSH tunnel to localhost.run with keepalive...')
    cmd = [
        'ssh',
        '-R', '80:127.0.0.1:8000',
        '-o', 'StrictHostKeyChecking=no',
        '-o', 'ServerAliveInterval=15',
        '-o', 'ServerAliveCountMax=3',
        '-o', 'ExitOnForwardFailure=yes',
        'nokey@localhost.run'
    ]
    
    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        current_url = None
        for line in iter(proc.stdout.readline, ''):
            print(line, end='', flush=True)
            m = re.search(r'https://[a-zA-Z0-9\-\.]+\.lhr\.life', line)
            if m:
                current_url = m.group(0)
                print(f'\n>>> ACTIVE TUNNEL URL: {current_url} <<<\n', flush=True)
                with open(tunnel_log_file, 'w') as f:
                    f.write(current_url)
                
                # Regenerate QR code
                try:
                    qr_path = r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\qr_public.png'
                    qr = qrcode.make(current_url)
                    qr.save(qr_path)
                    shutil.copy(qr_path, os.path.join(artifact_dir, 'qr_public.png'))
                except Exception as ex:
                    print('QR code update error:', ex)
                    
        proc.wait()
        print(f'SSH process ended with code {proc.returncode}. Reconnecting in 3 seconds...')
    except Exception as e:
        print('Tunnel error:', e)
    
    time.sleep(3)

qemu-system-x86_64 -enable-kvm -cpu host -m 3G -smp 2 -hda ./main.qcow2 -vnc :0 &
websockify --web ./noVNC-1.4.0 6080 localhost:5900


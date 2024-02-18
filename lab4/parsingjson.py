import json
with open(r"C:\Users\User\Desktop\python pp2\lab4\sample-data.json","r") as my_file:
    data = json.load(my_file)

    interfaces = data.get('imdata', [])
    
    print("Interface Status")
    print("=" * 79)
    print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
    print("-" * 79)
    
    for interface in interfaces:
        l1physif = interface.get('l1PhysIf', {}).get('attributes', {})
        dn = l1physif.get('dn', 'N/A')
        descr = l1physif.get('descr', 'N/A')  
        speed = l1physif.get('speed', 'inherit')
        mtu = l1physif.get('mtu', 'N/A')
        print("{:<50} {:<15} {:<10} {:<10}".format(dn, descr, speed, mtu))
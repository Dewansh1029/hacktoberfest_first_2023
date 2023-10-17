def get_mac_info(device, mac_addr):

    cmd = 'show mac address-table address {0} | json-pretty'.format(mac_addr)
    output = device.execute(cmd)
    mac_info = {}
    try:
       output_json = json.loads(output)
       if type(output_json) is dict:
         if type(output_json["TABLE_mac_address"]["ROW_mac_address"]) is dict:
            intf_1 = output_json["TABLE_mac_address"]["ROW_mac_address"]["disp_port"]
            vlan_1 = output_json["TABLE_mac_address"]["ROW_mac_address"]["disp_vlan"]
            mac_info[vlan_1] = intf_1
         elif type(output_json["TABLE_mac_address"]["ROW_mac_address"]) is list:
            len1 = len(output_json["TABLE_mac_address"]["ROW_mac_address"])          
            for i in range(0, len1):
               intf_1 = output_json["TABLE_mac_address"]["ROW_mac_address"][i]["disp_port"]
               vlan_1 = output_json["TABLE_mac_address"]["ROW_mac_address"][i]["disp_vlan"]
               mac_info[vlan_1] = intf_1
    except Exception as e:
       pass
    return mac_info

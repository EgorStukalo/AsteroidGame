def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices and device not in not_supported_devices:
        supported_catalog[device] = dict_devices[device]
    return supported_catalog  
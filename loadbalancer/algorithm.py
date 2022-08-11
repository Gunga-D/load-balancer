class RoundRobin():
    def __init__(self, servers):
        self.__current_server_index = -1
        self.__pool = servers
    
    def update_pool(self, servers):
        self.__pool = servers

    def get_server(self):
        self.__current_server_index += 1
        if self.__current_server_index >= len(self.__pool):
            self.__current_server_index = 0

        return self.__pool[self.__current_server_index]

class LeastConnections():
    def __init__(self, servers):
        self.__pool = {server: 0 for server in servers}
        print(self.__pool)

    def __find_missing_servers(self, servers):
        to_remove = [server for server in self.__pool if server not in servers]
        to_add = [server for server in servers if server not in self.__pool]
        return to_remove, to_add

    def __include_servers(self, servers):
        if servers is None:
            return
        for server in servers:
            self.__pool[server] = 0

    def __exlude_servers(self, servers):
        if servers is None:
            return
        for server in servers:
            del self.__pool[server]

    def update_pool(self, servers):
        to_remove, to_add = self.__find_missing_servers(servers)
        self.__exlude_servers(to_remove)
        self.__include_servers(to_add)
    
    def get_server(self):
        desired_server = min(self.__pool, key = self.__pool.get)
        self.__pool[desired_server] += 1
        return desired_server
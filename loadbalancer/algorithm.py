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
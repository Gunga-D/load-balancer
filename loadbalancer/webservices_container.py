class WebServicesContainer():
    def __init__(self, webservices):
        self.__active_pool = webservices
        self.__passive_pool = []
    
    def __len__(self):
        return len(self.__active_pool)

    def __repr__(self):
        return self.__active_pool.__repr__()

    def __getitem__(self, idx):
        return self.__active_pool[idx]

    def __iter__(self):
        return iter(self.__active_pool)

    def __contains__(self, webservice):
        return webservice in self.__active_pool

    def __add__(self, other):
        return self.__active_pool + other

    def activate(self, webservice):
        self.__active_pool.append(webservice)
        self.__passive_pool.remove(webservice)
    
    def deactivate(self, webservice):
        self.__active_pool.remove(webservice)
        self.__passive_pool.append(webservice)

    @property
    def passive(self):
        return self.__passive_pool
# -*- coding: utf-8 -*-
import xmlrpc.client


class XmlRPC:
    def __init__(self, url, db, login, password):
        self.url = url
        self.db = db
        self.login = login
        self.password = password
        self.uid = self.set_uid()
        self.models = self.set_models()

    def set_uid(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        return common.authenticate(self.db, self.login, self.password, {})

    def set_models(self):
        return xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def search(self, model, domains=[[]]):
        return self.models.execute_kw(self.db, self.uid, self.password, model, 'search', domains)

    def search_read(self, model, domains=[[]], fields=[]):
        return self.models.execute_kw(self.db, self.uid, self.password, model, 'search_read', domains, {'fields': fields})

    def create(self, model, values={}):
        return self.models.execute_kw(self.db, self.uid, self.password, model, 'create', [values])


if __name__ == "__main__":
    a = XmlRPC('http://10.10.50.94:8069', 'SCF', 'admin', '1')
    print(a.search_read('x.cashmove', fields=['id','user_id', 'amount']))


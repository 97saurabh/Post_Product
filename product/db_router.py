class App1DBRouter(object):
    """
    A router to control app1 db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'product':
            return 'product'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'product':
            return 'product'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in app1 is involved"
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'product' or obj2._meta.app_label == 'product':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the app1 app only appears on the 'app1' db"
        from django.conf import settings
        if 'product' not in settings.DATABASES:
            return None
        if db == 'product':
            return model._meta.app_label == 'product'
        elif model._meta.app_label == 'product':
            return False
        return None

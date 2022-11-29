class AuthRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        return "replica_1"

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'default'
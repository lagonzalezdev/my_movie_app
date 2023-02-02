from models.actor import Actor as ActorModels

class ActorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_actors(self) -> ActorModels:
        result = self.db.query(ActorModels).all()
        return result

    def create_actor(self,actor:ActorModels):
        new_actor = ActorModels(
        actor_first_name = actor.actor_first_name ,
        actor_last_name = actor.actor_last_name,
        actor_gender = actor.actor_gender,    
        )
        self.db.add(new_actor)
        self.db.commit()
        return
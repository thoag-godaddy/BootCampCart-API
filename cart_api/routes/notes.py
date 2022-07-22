import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseNote


class Note:
    def on_get(self, req, resp, note_id):
        note = DatabaseNote.get(id=note_id)
        resp.media = model_to_dict(note)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, note_id):
        DatabaseNote.delete_by_id(note_id)
        resp.status = falcon.HTTP_204


class NoteList:
    def on_get(self, req, resp):
        return_data = []
        note_list = DatabaseNote.select()
        for note in note_list:
            return_data.append(model_to_dict(note))

        resp.media = return_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        obj = req.get_media()
        new_note = DatabaseNote(
            url=obj.get('url'),
            title=obj.get('title'),
            description=obj.get('description'),
            image_url=obj.get('image_url'),
            hashtags=obj.get('hashtags')
        )
        new_note.save()
        resp.media = model_to_dict(new_note)
        resp.status = falcon.HTTP_201

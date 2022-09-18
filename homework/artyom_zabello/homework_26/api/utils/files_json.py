class JsonFiles:

    @staticmethod
    def json_create_meme(text, url, type_meme, size):
        meme = {
            "text": text,
            "url": url,
            "tags": ["meme", 12],
            "info": {"type": type_meme, "size": size}
        }
        return meme

    @staticmethod
    def json_update_meme(id_meme, text):
        meme = {
            "id": id_meme,
            "text": text,
            "url": "https://123.com",
            "tags": ["meme", 12],
            "info": {"size": "small", "type": "text"}
        }
        return meme

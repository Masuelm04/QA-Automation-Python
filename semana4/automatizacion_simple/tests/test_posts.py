from semana4.automatizacion_simple.services.post_service import PostService
from semana4.automatizacion_simple.utils.validators import Validators
from semana4.automatizacion_simple.utils.file_reader import FileReader

service = PostService()
fileReader = FileReader()
validator = Validators()

datos_posts = fileReader.read_json("semana4/automatizacion_simple/data/posts.json")

response, post = service.get_post(1)

validator.validar_status_code(response, 200)
validator.validar_campo_igual("id", 1, post.id)
validator.validar_campo_no_vacio("title", post.title)
validator.validar_campo_no_vacio("body", post.body)

print("GET post validado correctamente")

data_nuevo_post = datos_posts["nuevo_post"]

response, post_creado = service.post_post(data_nuevo_post)

validator.validar_status_code(response, 201)
validator.validar_campo_igual("title", data_nuevo_post["title"], post_creado.title)
validator.validar_campo_igual("body", data_nuevo_post["body"], post_creado.body)
validator.validar_campo_igual("userId", data_nuevo_post["userId"], post_creado.user_id)

print("POST post validado correctamente")

data_post_actualizado = datos_posts["post_actualizado"]

response, post_actualizado = service.put_post(1, data_post_actualizado)

validator.validar_status_code(response, 200)
validator.validar_campo_igual("title", data_post_actualizado["title"], post_actualizado.title)
validator.validar_campo_igual("body", data_post_actualizado["body"], post_actualizado.body)

print("PUT post validado correctamente")

data_patch = {
    "title": "Título actualizado parcialmente"
}

response, post_patch = service.patch_post(1, data_patch)

validator.validar_status_code(response, 200)
validator.validar_campo_igual("title", data_patch["title"], post_patch.title)

print("PATCH post validado correctamente")

response = service.delete_post(1)

validator.validar_status_code(response, 200)

print("DELETE post validado correctamente")
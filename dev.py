from livereload import Server

server = Server()

server.watch("static/styles.css")

server.serve(
    root=".",
    port=5500,
)
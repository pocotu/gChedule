const http = require("http");
const fs = require("fs");
const path = require("path");

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        fs.readFile(path.join(__dirname, "index.html"), (err, data) => {
            if (err) {
                res.writeHead(500, { "Content-Type": "text/plain" });
                res.end("Error interno del servidor");
            } else {
                res.writeHead(200, { "Content-Type": "text/html" });
                res.end(data);
            }
        });
    } else if (req.url === "/archivos") {
        const files = fs.readdirSync(path.join(__dirname, "catalogos"));
        const xlsFiles = files.filter(file => path.extname(file) === ".xls");

        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify(xlsFiles));
    } else if (req.url.endsWith(".xls")) {
        const filePath = path.join(__dirname, "catalogos", req.url);
        
        fs.readFile(filePath, (err, data) => {
            if (err) {
                res.writeHead(500, { "Content-Type": "text/plain" });
                res.end("Error al leer el archivo");
            } else {
                res.writeHead(200, { "Content-Type": "application/octet-stream" });
                res.end(data);
            }
        });
    } else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end("Página no encontrada");
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Servidor en funcionamiento en http://localhost:${PORT}`);
});

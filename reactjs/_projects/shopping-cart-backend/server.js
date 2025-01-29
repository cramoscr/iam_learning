var express = require('express');
var mongoose = require('mongoose');
var cors = require('cors');
var dotenv = require('dotenv');

//import productRoutes from './routes/productRoutes.js';

dotenv.config();

var app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5000;

mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log("MongoDB conectado"))
.catch(err => console.error(err));

app.get("/", (req, res) => {
  res.send("API funcionando 🚀");
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});

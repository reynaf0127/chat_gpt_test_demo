import { Configuration, OpenAIApi} from "openai";
import express from "express"; 
import bodyParser from "body-parser"; 
import cors from "cors"; 
//
import path from 'path';
const __dirname = path.resolve();
//
const configuration = new Configuration ({
    organization: "org-2UelCPtTtVYmfM2kt6ZrYRvL", 
    apiKey: "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", 

});

const openai = new OpenAIApi(configuration); 

const app = express(); 
const port = 3000; 

app.use(bodyParser.json()); 
app.use(cors()); 


app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
  });


app.post("/", async(req, res) => {
    const { message } = req.body;

    const completion = await openai.createChatCompletion({
        model: "gpt-3.5-turbo", 
        messages: [
            {role: "user", content: `${message}`}, 
        ]
    })

    res.json({
        completion: completion.data.choices[0].message
    })

});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});
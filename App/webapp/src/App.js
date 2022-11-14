import React from "react";
import { useState } from "react";

function App() {

  const API_URL = 'http://localhost:8000';
  const [form, setForm] = useState({ "text": '' });
  const [prediction, setPrediction] = useState(""); 


  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (form.text.length > 0) {
      predictPost(form)
      //setForm({ "text": '' })
    }
  }

  const predictPost = async (post) => {
    const bod = {
      "records":[post]
    }
    console.log(bod)
    const requestOptions = {
      method: 'POST',
      headers: {
        "Content-type": "application/json"
      },
      body: JSON.stringify(bod)
    };

    const response = await fetch(`${API_URL}/predict`, requestOptions)
    const data = await response.json();
    console.log(data.Predictions[0])
    const prediction = data.Predictions[0] ? "Posible Suicidio" : "Posible No Suicidio"
    setPrediction(prediction)
  }
  return (
    <div>
      <div className="text-center">
        <header className="p-3 bg-dark text-white">
          <h1 className="fw-light">Potential Suicides Prediction from Reddit Posts</h1>
        </header>

      </div>
      <div className="bg-light">
        <div className="row">
          <div className="col p-3 border border-primary border-2">
            <h2 className="fw-light" align="center">Reddit Post Info</h2>

            <form onSubmit={handleSubmit}>
              <div className="mb-3">
                <label htmlFor="text" className="form-label">Post Text: </label>
                <textarea className="form-control" type="number" id = "text" name = "text" value = {form.text} onChange={handleChange} rows = "5"></textarea>
              </div>
              <input className ="btn btn-primary" type = "submit"></input>
            </form>


          </div>
          <div className="col p-3 bg-light" align="center">
            {
              prediction !== "" ? (<p>{prediction}</p>) : (<></>)
            }
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

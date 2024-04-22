import React from 'react';
import './App.css'; // Import CSS file for styling

const InputForm = () => {
    return (
      <div style={{ textAlign: 'center' }}>
      <div className='inputbox'>
        <h2>PASSENGERS PREDICTION</h2>
        <p>Age</p>
        <input
          type="text"
          name="input1"
          placeholder="Enter the value"
        /><br/>
        <p>Tonnage</p>
        <input
          type="text"
          name="input2"
          placeholder="Enter the value"
        /><br/>
        <p>Length</p>
        <input
          type="text"
          name="input3"
          placeholder="Enter the value"
        /><br/>
        <p>Cabins</p>
        <input
          type="text"
          name="input4"
          placeholder="Enter the value"
        /><br/>
        <p>Passenger_density</p>
        <input
          type="text"
          name="input5"
          placeholder="Enter the value"
        /><br/>
        <p>Crew</p>
        <input
          type="text"
          name="input6"
          placeholder="Enter the value"
        /><br/>
      </div><br/>
      <button>Predict</button>
    </div>

    );
}

export default InputForm;
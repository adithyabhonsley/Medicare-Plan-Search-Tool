import { Button, TextField } from '@material-ui/core';
import React, { Fragment, useState } from 'react';
import './App.css';
import medicare from './medicare.json';

const App = () => {

  // State management for the Bid ID and matching details
  const [bidId, setBidId] = useState('');
  const [bid, setBid] = useState({});

  // Function to show content based on the state
  // If a valid bid ID is entered, it'll show all the fields of the provider
  // If an invalid Bid is entered, it shows error
  const viewBid = () => {
    if (!bid) {
      return <div>
        Invalid Bid ID Entered
        <br />
        Please enter a valid Bid ID
      </div>
    }
    if (Object.keys(bid).length > 0) {
      return <div id="table">
        {
          Object.keys(bid).map((key) => {
            if (bid[key] && bid[key] !== "\n") {
              return <div>
                <p className="title">
                  {key}
                </p>
                <p >
                  {bid[key]}
                </p>
              </div>
            } else {
              return <Fragment />
            }
          })
        }
      </div>
    }
    return <div>
      Enter a Bid ID and submit to load details
      </div>
  }

  return (
    <div id="container">
      <p id="heading">
      🔍 Medicare Plan Search-Up Tool
      </p>
      <TextField value={bidId} onChange={(e) => setBidId(e.target.value)} placeholder="Enter Bid ID" label="Bid ID" />
      <br />
      <Button variant="contained" color="secondary" onClick={() => {
        if (bidId && bidId.trim())
          setBid(medicare[bidId]);
      }}>
        Submit
      </Button>
      <div id="details">
        {viewBid()}
      </div>
    </div>
  );
}

export default App;
import React from 'react'
import {render} from 'react-dom';

  const TimetableSlot = (props) => {
    return(
      <div>
      {props.name}
      <br/>
      {props.room}
      </div>
    );
  }


export default TimetableSlot;

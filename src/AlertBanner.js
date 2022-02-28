import React from 'react';
import "./Styling/AlertBanner.css";

function AlertBanner(props) {
  const studentState = props.studentState;
  return (
    <div className="alert_banner">Student is {studentState}</div>
  )
}

export default AlertBanner
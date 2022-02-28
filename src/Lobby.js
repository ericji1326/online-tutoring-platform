import React from "react";
import { Form, Checkbox } from "semantic-ui-react";

function Lobby(props) {
  const username = props.username;
  const userNameChangeHandler = props.userNameChangeHandler;
  const roomName = props.roomName;
  const roomNameChangeHandler = props.roomNameChangeHandler;
  const submitHandler = props.submitHandler;
  const student_tutor = props.student_tutor;
  const set_student_tutor = props.student_tutor_ChangeHandler;
  return (
    <div>
      <form className="submitForm" onSubmit={submitHandler}>
        <h2>Start Session</h2>
        <div>
          <input
            className = "inputField"
            placeholder="Your Name"
            type="text"
            id="field"
            value={username}
            onChange={userNameChangeHandler}
            resolve
          />
        </div>

        <div>
          <input
            className = "inputField"
            placeholder="Classroom Name"
            type="text"
            id="room"
            value={roomName}
            onChange={roomNameChangeHandler}
            resolve
          />
        </div>

        <Form>
          <Form.Field className = "roleText">
            Role: <b>{student_tutor}</b>
          </Form.Field>
          <Form.Field>
            <Checkbox
              className = "checkbox"
              radio
              label=" Student"
              name="checkboxRadioGroup"
              value="Student"
              checked={student_tutor === "Student"}
              onChange={(e, data) => set_student_tutor(data.value)}
            />
          </Form.Field>
          <Form.Field>
            <Checkbox
              className = "checkbox"
              radio
              label=" Tutor"
              name="checkboxRadioGroup"
              value="Tutor"
              checked={student_tutor === "Tutor"}
              onChange={(e, data) => set_student_tutor(data.value)}
            />
          </Form.Field>
        </Form>
        <div className="buttonHolder">
          <button className="submitButton" type="submit">Enter Classroom</button>
        </div>
      </form>
    </div>
  );
}

export default Lobby;

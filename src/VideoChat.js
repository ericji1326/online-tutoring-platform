import React, { useState, useCallback } from "react";
import Lobby from "./Lobby";
import Room from "./Room";

function VideoChat() {
  const [username, setUsername] = useState("");
  const [roomName, setRoomName] = useState("");
  const [token, setToken] = useState(null);
  const [student_tutor, set_student_tutor] = useState("");
  
  const userNameChangeHandler = useCallback((event) => {
    setUsername(event.target.value);
  }, []);

  const roomNameChangeHandler = useCallback((event) => {
    setRoomName(event.target.value);
  }, []);

  const submitHandler = useCallback(
    async (event) => {
      event.preventDefault();
      const data = await fetch("/video/token", {
        method: "POST",
        body: JSON.stringify({
          identity: `${student_tutor} : ${username}`,
          room: roomName,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      }).then((res) => res.json());
      setToken(data.token);
    },
    [username, roomName, student_tutor]
  );

  const logoutHandler = useCallback((event) => {
    setToken(null);
  }, []);

  return (
    <div>
      {token ? (
        <Room roomName={roomName} token={token} logoutHandler={logoutHandler} />
        ) : (
        <Lobby
          username={username}
          roomName={roomName}
          student_tutor={student_tutor}
          student_tutor_ChangeHandler={set_student_tutor}
          userNameChangeHandler={userNameChangeHandler}
          roomNameChangeHandler={roomNameChangeHandler}
          submitHandler={submitHandler}
        />
      )}
    </div>
  );
}

export default VideoChat;

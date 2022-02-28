import React, { useState, useEffect, useRef } from "react";
import Video from "twilio-video";
import Participant from "./Participant";
import { db } from "./Firebase";
import { useScreenshot } from "use-react-screenshot";
import "./Styling/Room.css";
import {
  query,
  collection,
  getDocs,
  setDoc,
  where,
  doc,
} from "firebase/firestore";
import axios from "axios";
import AlertBanner from "./AlertBanner";
import FadeIn from "react-fade-in";

function Room(props) {
  const ref = useRef(null);

  const base64ref = useRef(null);

  const [image, takeScreenshot] = useScreenshot({
    type: "image/jpeg",
    quality: 1.0,
  });
  const roomName = props.roomName;
  const token = props.token;
  const logoutHandler = props.logoutHandler;
  //const [imageString, setImageString] = useState("");

  var isTutor = false;

  const [room, setRoom] = useState(null);
  const [participants, setParticipants] = useState([]);
  const [studentState, setStudentState] = useState(true);

  const remoteParticipants = participants.map((participant) => (
    <Participant key={participant.sid} participant={participant} />
  ));

  useEffect(() => {
    async function getImage() {
      if (ref.current !== null) {
        takeScreenshot(ref.current); // Updates the image based on ss
        // console.log(imageString);
        var base64 = document.getElementById("base64");
        console.log(base64?.src);

        // If Base64 Image String Not Null, Add To DB
        if (base64?.src) {
          console.log("RUN");
          try {
            const userDocRef = doc(
              db,
              "base64_image_collection",
              "base_64_img"
            );
            setDoc(userDocRef, { img_str: base64?.src }, { merge: true });
          } catch (err) {
            alert(err);
          }
        }
        // Nudge the Backend
        try {
          const { data } = await axios(`http://localhost:5000/model1`);
          console.log(data.expression);
          setStudentState(data.expression);
          // Set the State of Confusion Here
        } catch (err) {
          alert(err);
        }
      }
      setTimeout(() => {
        getImage();
      }, 1000);
    }
    getImage();
  }, []);

  useEffect(() => {
    const participantConnected = (participant) => {
      setParticipants((prevParticipants) => [...prevParticipants, participant]);
    };
    const participantDisconnected = (participant) => {
      setParticipants((prevParticipants) =>
        prevParticipants.filter((p) => p !== participant)
      );
    };
    Video.connect(token, {
      name: roomName,
    }).then((room) => {
      setRoom(room);
      room.on("participantConnected", participantConnected);
      room.on("participantDisconnected", participantDisconnected);
      room.participants.forEach(participantConnected);
    }, []);

    return () => {
      setRoom((currentRoom) => {
        if (currentRoom && currentRoom.localParticipant.state === "connected") {
          currentRoom.localParticipant.tracks.forEach(function (
            trackPublication
          ) {
            trackPublication.track.stop();
          });
          currentRoom.disconnect();
          return null;
        } else {
          return currentRoom;
        }
      });
    };
  }, [roomName, token]);

  if (
    room?.localParticipant.identity &&
    room?.localParticipant?.identity.split(":")[0] === "Tutor "
  ) {
    isTutor = true;
  }

  return (
    <div className="room">
      <button className="logoutButton" onClick={logoutHandler}>
        Log out
      </button>
      <div className="local-participant">
        {room ? (
          <Participant
            key={room.localParticipant.sid}
            participant={room.localParticipant}
          />
        ) : (
          ""
        )}
      </div>

      <div className="remote-participants">
        <div ref={ref}>{remoteParticipants}</div>
        {isTutor ? (
          <div>
            <img id="base64" src={image} style={{ display: "None" }} alt="">
              {/* {console.log(image)} */}
              {/* {setImageString(image)} */}
            </img>
            {studentState !== "No Face" ? (
              <FadeIn delay={300}>
                <AlertBanner studentState={studentState} />
              </FadeIn>
            ) : (
              ""
            )}
            {/* Render a BANNER */}
          </div>
        ) : (
          ""
        )}
      </div>
    </div>
  );
}

export default Room;

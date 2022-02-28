import { initializeApp } from "firebase/app";
import {
  getFirestore,
  query,
  getDocs,
  collection,
  where,
  addDoc,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyD6R9LrVgGkVmJJlz1a9gqIGIPBAKyIoGc",
  authDomain: "levelup-dcde9.firebaseapp.com",
  projectId: "levelup-dcde9",
  storageBucket: "levelup-dcde9.appspot.com",
  messagingSenderId: "298756067717",
  appId: "1:298756067717:web:99f93a67ff65d4cfd834ec",
  measurementId: "G-VHYC3CPVE1",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export { db };

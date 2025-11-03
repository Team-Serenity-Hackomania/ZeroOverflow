import { useState } from "react";
import "./App.css";

function App() {
  const [state, setState] = useState("");
  const [city, setCity] = useState("");
  const [locality, setLocality] = useState("");
  const [person, setPerson] = useState("");
  const [attendance, setAttendance] = useState("");
  const [date, setDate] = useState("");

  const data = {
    Maharashtra: {
      Mumbai: ["Andheri", "Bandra", "Borivali"],
      Pune: ["Shivaji Nagar", "Hinjewadi", "Kothrud"],
    },
    Karnataka: {
      Bengaluru: ["Koramangala", "Whitefield", "Indiranagar"],
      Mysuru: ["Vijayanagar", "Lakshmipuram"],
    },
    Delhi: {
      "New Delhi": ["Connaught Place", "Saket", "Dwarka"],
    },
  };

  const people = ["Rahul Sharma", "Aditi Verma", "Rohan Das", "Sneha Patil"];

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!state || !city || !locality || !person || !attendance || !date) {
      alert("Please fill out all fields!");
      return;
    }
    alert(
      `✅ Attendance recorded:\n\nDate: ${date}\nName: ${person}\nLocation: ${locality}, ${city}, ${state}\nStatus: ${attendance}`
    );
    setState("");
    setCity("");
    setLocality("");
    setPerson("");
    setAttendance("");
    setDate("");
  };

  return (
    <div className="app-container">
      <h1>Attendance Tracker</h1>

      <form onSubmit={handleSubmit} className="attendance-form">
        <label>Date:</label>
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />

        <label>State:</label>
        <select value={state} onChange={(e) => setState(e.target.value)}>
          <option value="">Select State</option>
          {Object.keys(data).map((st) => (
            <option key={st} value={st}>
              {st}
            </option>
          ))}
        </select>

        <label>City:</label>
        <select
          value={city}
          onChange={(e) => setCity(e.target.value)}
          disabled={!state}
        >
          <option value="">Select City</option>
          {state &&
            Object.keys(data[state]).map((ct) => (
              <option key={ct} value={ct}>
                {ct}
              </option>
            ))}
        </select>

        <label>Locality:</label>
        <select
          value={locality}
          onChange={(e) => setLocality(e.target.value)}
          disabled={!city}
        >
          <option value="">Select Locality</option>
          {city &&
            data[state][city].map((loc) => (
              <option key={loc} value={loc}>
                {loc}
              </option>
            ))}
        </select>

        <label>Person:</label>
        <select
          value={person}
          onChange={(e) => setPerson(e.target.value)}
        >
          <option value="">Select Person</option>
          {people.map((p) => (
            <option key={p} value={p}>
              {p}
            </option>
          ))}
        </select>

        <label>Attendance:</label>
        <select
          value={attendance}
          onChange={(e) => setAttendance(e.target.value)}
        >
          <option value="">Mark Attendance</option>
          <option value="Present">Present</option>
          <option value="Absent">Absent</option>
          <option value="Late">Late</option>
        </select>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;

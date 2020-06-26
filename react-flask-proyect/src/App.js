import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
    const [currentTime, setCurrentTime] = useState(0);
    const [value, handlerVal] = useState(0);
    const [mssg, handlerMssg] = useState('aja');
    useEffect(() => {
        fetch('/time').then(res => res.json()).then(data => {
        setCurrentTime(data.time);
        });
    }, []);
    useEffect(() => {
        fetch('/test').then(res => res.json()).then(data => {
        handlerVal(data.a);
        });
    }, []);
    useEffect(() => {
        fetch('/blog/create').then(res => res.json()).then(data => {
        handlerMssg(data.create);
        });
    }, []);

    return (
    <div className="App">
        <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Edit <code>src/App.js</code> and save to reload.</p>
        <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
            Learn React
        </a>
        <p>The current time is {currentTime}.</p>
        <p>The value is {mssg}.</p>
        </header>
    </div>
    );
}

export default App;

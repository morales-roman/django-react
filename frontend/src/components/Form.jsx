import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';
import api from '../api';

function Form({ route, method }) {
    const [username, setUsername] = userState('');
    const [password, setPassword] = userState('');
    const [loading, setLoading] = userState(false);
    const navigate = useNavigate();

    const name = method === "login" ? "Login" : "Register";

    const handleSubmit = async (event) => {
        setLoading(true);
        event.preventDefault();
        try {
            const response = await api.post(route, { username, password });
            if (method === "login") {
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
                navigate('/');
            }
            else {
                navigate('/login');
            }
        }
        catch (error) {
            console.error(error);
        }
        finally {
            setLoading(false);
        }
    }

    return (
        <form onSubmit={handleSubmit} className='form-container'>
            <h1>{name}</h1>
            <label htmlFor="username">Username</label>
            <input
                className='form-input'
                type="text"
                id="username"
                value={username}
                onChange={(event) => setUsername(event.target.value)}
                placeholder="Username"
            />
            <label htmlFor="password">Password</label>
            <input
                type="password"
                id="password"
                className='form-input'
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                placeholder='Password'
            />
            <button type="submit" className='form-button'>
                {name}
            </button>
        </form>
    );
}
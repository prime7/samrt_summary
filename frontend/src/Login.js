import React, { useState } from 'react'
import axios from 'axios'
import { LOGIN } from './API'

export default function Login() {
    const [username,setUsername] = useState("")
    const [password,setPassword] = useState("")

    const loginUser = () =>{
        const config = {
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const body = JSON.stringify({
            username:  username,
            password:  password
        });

        axios
        .post(LOGIN, body, config)
        .then((res) => {
            localStorage.setItem('smrtsmry-user',res.data.token)
            window.location.href = '/'; 
        })
        .catch((err) => {
            console.error(err)
        });
    }

    return (
        <div className="form">
            <div className="form-login">
                <div className="form-floating">
                    <input type="text" className="form-control" id="floatingInput" placeholder="Username" value={username} onChange={e=>setUsername(e.target.value)}/>
                    <label htmlFor="floatingInput">Username</label>
                </div>
                <div className="form-floating">
                    <input type="password" className="form-control" id="floatingPassword" placeholder="Password" value={password} onChange={e=>setPassword(e.target.value)}/>
                    <label htmlFor="floatingPassword">Password</label>
                </div>
                <button className="w-100 btn btn-lg btn-primary" onClick={loginUser}>Sign in</button>
            </div>
        </div>
    )
}

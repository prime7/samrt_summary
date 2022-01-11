import React, { useState } from 'react'
import axios from 'axios'
import { REGISTER } from './API'

export default function Register() {
    const [username,setUsername] = useState("")
    const [password1,setPassword1] = useState("")
    const [password2,setPassword2] = useState("")

    const passwordNotMatch = password1 !== password2;
    const registerUser = () =>{
        const config = {
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const body = JSON.stringify({
            username:  username,
            password1:  password1,
            password2:  password2,
        });

        axios
        .post(REGISTER, body, config)
        .then((res) => {
            window.location.href = '/login'; 
        })
        .catch((err) => {
            console.error(err)
        });
    }

    return (
        <div className="form">
            <div className="form-login">
                {passwordNotMatch && (
                    <div className="alert alert-danger" role="alert">
                        Password did not match.
                    </div>
                )}
                <div className="form-floating">
                    <input type="text" className="form-control" id="floatingInput" placeholder="Username" value={username} onChange={e=>setUsername(e.target.value)}/>
                    <label for="floatingInput">Username</label>
                </div>
                <div className="form-floating">
                    <input type="password" className="form-control" id="floatingPassword1" placeholder="Password" value={password1} onChange={e=>setPassword1(e.target.value)}/>
                    <label for="floatingPassword1">Password</label>
                </div>
                <div className="form-floating">
                    <input type="password" className="form-control" id="floatingPassword2" placeholder="Confirm Password" value={password2} onChange={e=>setPassword2(e.target.value)}/>
                    <label for="floatingPassword2">Confirm Password</label>
                </div>
                <button className="w-100 btn btn-lg btn-primary" onClick={registerUser}>Sign up</button>
            </div>
        </div>
    )
}

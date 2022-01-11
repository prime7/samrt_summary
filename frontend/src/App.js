import React from 'react'
import Footer from './Footer'
import Menu from './Menu'
import Summary from './Summary'
import Login from './Login'
import Register from './Register'
import {
    BrowserRouter as Router,
    Switch,
    Route,
} from "react-router-dom"


export default function App() {
    return (
        <div>
            <Menu />
            <div className="body">
                <Router>
                    <Switch>
                        <Route exact path="/"><Summary /></Route>
                        <Route exact path="/login"><Login /></Route>
                        <Route exact path="/register"><Register /></Route>
                    </Switch>
                </Router>
            </div>
            <Footer />
        </div>
    )
}
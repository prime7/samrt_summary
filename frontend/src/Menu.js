import React from 'react'
import {
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink
} from 'reactstrap';

export default function Menu() {
    const loggedIn = localStorage.getItem('smrtsmry-user')
    const logout = () => {
        localStorage.removeItem('smrtsmry-user')
        window.location.href = '/';
    }
    return (
        <Navbar color="dark" dark expand="md" className="p-3">
            <NavbarBrand href="/">Smart-Summary</NavbarBrand>
            <Nav navbar>
                <NavItem>
                    <NavLink href="/">Home</NavLink>
                </NavItem>
                {loggedIn? 
                <button type="button" className="btn btn-primary"onClick={logout}>Logout</button>:
                <NavItem>
                    <NavLink href="/login/">Login</NavLink>
                </NavItem>
                }
            </Nav>
        </Navbar>
    )
}

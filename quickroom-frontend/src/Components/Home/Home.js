import React, { useEffect, useState } from 'react'

export default function Home() {

  const [email, setEmail] = useState('');
  const [role,setRole] = useState('');

  useEffect(()=>{
    const storedEmail = localStorage.getItem('email'); 
    const storedRole = localStorage.getItem('role');
    setEmail(storedEmail);
    setRole(storedRole);
  },[])

  return (
    <div>
    <div>
    <h1>Home Page</h1>
    {email ? <p>Email: {email}</p> : <p>User is not logged in</p>}
    {role ? <p>Role: {role}</p> : <p>Role not available</p>}
    </div>
    </div>
  )
}

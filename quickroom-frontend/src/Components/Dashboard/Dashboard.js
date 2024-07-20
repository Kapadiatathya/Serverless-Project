import React from 'react'
import Navbar from '../Navbar/Navbar'

export default function Dashboard() {
  return (
    <>
    <Navbar></Navbar>
    <h1>Dashboard</h1>
    <iframe
        src={"https://lookerstudio.google.com/embed/reporting/66a1d258-ec31-420c-a46e-35ef6aa2716b/page/5Oa6D"}
        title="Embedded Content"
        width="80%"
        height="600px"
        style={{ border: 'none' }}
      />
    </>
    
  )
}

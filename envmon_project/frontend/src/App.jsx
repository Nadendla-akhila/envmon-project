import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts'

function App(){
  const [readings, setReadings] = useState([])
  useEffect(()=>{
    async function load(){
      const res = await axios.get('/api/readings?limit=200')
      setReadings(res.data.map(r=>({
        timestamp: new Date(r.timestamp).toLocaleString(),
        pm25: r.pm25
      })))
    }
    load()
    const t = setInterval(load, 15000)
    return ()=>clearInterval(t)
  }, [])

  return (
    <div style={{padding:20,fontFamily:'Arial'}}>
      <h1>Environmental Monitoring Dashboard</h1>
      <p>Live PM2.5</p>
      <div style={{width:'100%',height:300}}>
        <ResponsiveContainer>
          <LineChart data={readings}>
            <XAxis dataKey="timestamp" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="pm25" dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}

export default App

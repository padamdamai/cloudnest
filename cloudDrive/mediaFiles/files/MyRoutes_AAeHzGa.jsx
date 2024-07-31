import React from 'react'
import {  BrowserRouter, Route, Routes } from 'react-router-dom'
import First from './First'
import Layouts from './components/Layouts'


const MyRoutes = () => {
  return (
  <BrowserRouter>
    <Routes>
       <Route path='/' element={<Layouts/>}>
          <Route index element={<First/>}/>
          </Route>
    </Routes>
  </BrowserRouter>
  )
}

export default MyRoutes
import React, { Component } from 'react'
import axios from 'axios'
export default class Main extends Component {
  debugger
  state = {
    value:[]
  }

  getData = async() =>{
    let value = await axios.get(`http://127.0.0.1:8000/doctors_list`)
    debugger
    let data = await value.data
    this.setState({value: data})     
  }
  
  componentDidMount(){
    this.getData()
    // fetch('http://127.0.0.1:8000/doctors_list').then((resp)=>resp.json()).then(doctors_list=>{this.setState({list:doctors_list})})
    debugger
  }

  render() {
    return (
      <div>Main</div>
    )
  }
}

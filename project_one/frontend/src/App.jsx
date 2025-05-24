import { useState, useEffect } from 'react'
import './App.css'
import ContactList from './ContactList'
import ContactForm from './ContactForm'


function App() {
  const [contacts, setContacts]=useState([])
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentContact, setCurrentContact]=useState({})


  useEffect(()=>{
    fetchContacts()
  }, [])
  const fetchContacts= async() => {
    const response= await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts) 
    console.log(data.contacts)
  }

  const closeModal=()=>{
    setIsModalOpen(false)
    setCurrentContact({})
  }

  const openCreateModal=()=>{
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal=(contacts)=>{
    if (isModalOpen) return 
    setCurrentContact(contacts)
    setIsModalOpen(true)
  }

  const onUpdate=() =>{
    closeModal()
    fetchContacts()
  }

  return <><ContactList contacts={contacts} updateContact={openEditModal}/>
  <button onClick={openCreateModal}>Create New Contact</button>
  {
    isModalOpen && <div className="modal">
      <div className="modal-content">
        <span className='close' onClick={closeModal}>&times;</span>
        <ContactForm existingContact={currentContact} updateCalback={onUpdate}/>

      </div>
    </div>
  }
  </>
}

export default App

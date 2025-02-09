import React, { useEffect, useState } from 'react';
import Navbar from '../Navbar/Navbar';
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import Typography from '@mui/material/Typography';

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
    <>
    <Navbar></Navbar>
    <Box sx={{ width: 'auto', height: 'auto', padding: 2, bgcolor: '#f5f5f5', borderRadius: 2}}>
        <Typography variant="h4" component="h1" gutterBottom sx={{ fontWeight: 'bold', color: '#3f51b5' }}>
          Dal Vacation Home
        </Typography>
        <Typography variant="body1" paragraph sx={{ fontSize: '1.1rem', color: '#555' }}>
          Welcome to Dal Vacation Home, your perfect getaway destination! Whether you're looking to book a room for a relaxing vacation or a productive business trip, we offer a range of accommodations to suit your needs. Enjoy a comfortable stay with us, featuring well-appointed rooms and top-notch amenities. Book your room today and experience the best of hospitality.
        </Typography>
      </Box>
    <Box sx={{ width: 'auto', height: 'auto' }}>
      <ImageList variant="masonry" cols={3} gap={8}>
        {itemData.map((item) => (
          <ImageListItem key={item.img}>
            <img
              srcSet={`${item.img}?w=248&fit=crop&auto=format&dpr=2 2x`}
              src={`${item.img}?w=248&fit=crop&auto=format`}
              alt={item.title}
              loading="lazy"
            />
          </ImageListItem>
        ))}
      </ImageList>
    </Box>
    </>
  )
}

const itemData = [
  {
    img: 'https://images.unsplash.com/photo-1549388604-817d15aa0110',
    title: 'Bed',
  },
  {
    img: 'https://images.unsplash.com/photo-1525097487452-6278ff080c31',
    title: 'Books',
  },
  {
    img: 'https://images.unsplash.com/photo-1523413651479-597eb2da0ad6',
    title: 'Sink',
  },
  {
    img: 'https://images.unsplash.com/photo-1563298723-dcfebaa392e3',
    title: 'Kitchen',
  },
  {
    img: 'https://images.unsplash.com/photo-1588436706487-9d55d73a39e3',
    title: 'Blinds',
  },
  {
    img: 'https://images.unsplash.com/photo-1574180045827-681f8a1a9622',
    title: 'Chairs',
  },
  {
    img: 'https://images.unsplash.com/photo-1530731141654-5993c3016c77',
    title: 'Laptop',
  },
  {
    img: 'https://images.unsplash.com/photo-1481277542470-605612bd2d61',
    title: 'Doors',
  },
  {
    img: 'https://images.unsplash.com/photo-1517487881594-2787fef5ebf7',
    title: 'Coffee',
  },
  {
    img: 'https://images.unsplash.com/photo-1516455207990-7a41ce80f7ee',
    title: 'Storage',
  },
  {
    img: 'https://images.unsplash.com/photo-1597262975002-c5c3b14bbd62',
    title: 'Candle',
  },
  {
    img: 'https://images.unsplash.com/photo-1519710164239-da123dc03ef4',
    title: 'Coffee table',
  },
];

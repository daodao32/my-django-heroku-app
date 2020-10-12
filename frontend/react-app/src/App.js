import React from 'react';
import './App.css';
import 'antd/dist/antd.css'

import CustomLayout from './components/containers/Layout';
import PostLists from './components/containers/listview';

function App() {
  return (
    <div className="App">
      <CustomLayout>
      <PostLists />
      </CustomLayout>
    </div>
  );
}

export default App;

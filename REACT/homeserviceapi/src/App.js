import React, { useEffect, useState } from 'react';
import './App.css';
import Jobs from './components/Jobs';
import JobLoadingComponent from './components/JobLoading';

function App() {
  const JobLoading = JobLoadingComponent(Jobs);
  const [appState, setAppState] = useState({
    loading: false,
    jobs: null,
  });
  useEffect(() => {
    setAppState({ loading : true});
    const apiUrl = 'http://127.0.0.1:8000/api/';
    fetch(apiUrl).then((data) => data.json())
    .then((jobs) => {
      setAppState({ loading : false, jobs : jobs });
    });
  }, [setAppState]);
  return(
    <div className="App">
      <h1>Available Jobs</h1>
      <JobLoading isLoading={appState.loading} jobs={appState.jobs} />
    </div>
  );
}

export default App;
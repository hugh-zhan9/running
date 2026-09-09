import './styles/index.css';
import { Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import Index from './pages/index';
import HomePage from './pages/total';
import SummaryRoutePage from './pages/summary';
import NotFound from './pages/404';
import { ActivitiesProvider } from './contexts/ActivitiesContext';

export default function ClassicTheme() {
  return (
    <HelmetProvider>
      <BrowserRouter basename={import.meta.env.BASE_URL}>
        <Suspense fallback={<div>Loading...</div>}>
          <ActivitiesProvider>
            <Routes>
              <Route path="/" element={<Index />} />
              <Route path="summary" element={<HomePage />} />
              <Route path="summary/:year" element={<SummaryRoutePage />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </ActivitiesProvider>
        </Suspense>
      </BrowserRouter>
    </HelmetProvider>
  );
}

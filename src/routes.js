import React from 'react'
import { Route, IndexRoute } from 'react-router'
import { Main } from './home/main'
import App from './components/App'

export default (
  <Route path="/" component={App}>
    <IndexRoute component={Main}/>
  </Route>
)

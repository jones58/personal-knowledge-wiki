---
title: Redux
---

Redux is used for global state management.

# Store

Actions - show what happens in application. Have a type field.
Reducer - shows result of action - receives current state and action, and works out new state (state,action) => newState
Dispatch - function to send action to update store. sends action to different reducers

Slices - split features into separate reducers and group them together in a store.

Don't mutate state with reducers (unless using Immer).

Thunks - redux function that contains async logic (they otherwise can't) - `createAsyncThunk()`

useSelector() - this helps us read from the Redux store
useDispatch() - const dispatch = useDispatch() - then access the dispatchj acion with dispatch(name of function())

# Links

[Redux docs are a good place to start](https://redux.js.org/tutorials/essentials)

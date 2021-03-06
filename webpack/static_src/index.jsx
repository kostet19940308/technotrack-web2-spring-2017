/* global document: true */
/* global window: true */
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import './styles/bootstrap-3/css/bootstrap.css';

import LayoutComponent from './components/layout';
import PostListLayoutComponent from './components/postListLayout';


class Page extends Component {
    state = {
        postList: [],
        isLoading: true,
        user: {
            id: 0,
            username: '',
        },
    };

    render() {
        return (
            <MuiThemeProvider>
                <LayoutComponent>
                    <PostListLayoutComponent />
                </LayoutComponent>
            </MuiThemeProvider>
        );
    }
}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);
/* global document: true */
/* global window: true */
import React, { Component } from 'react';
import { Grid, Col } from 'react-bootstrap';
import '../styles/bootstrap-3/css/bootstrap.css';
import NavbarTop from './navbarTop';
import NavbarLeft from './navbarLeft';
import PostListLayoutComponent from './postListLayout';

class LayoutComponent extends Component {
    state = {
        user: {
            id: 0,
            username: '',
        },
        currentPageName: 'news',
    };

    componentDidMount() {
        fetch('http://localhost:8000/api/v1/users/?myself&format=json',
            {
                method: 'GET',
                credentials: 'same-origin',
            })
            .then(promise => promise.json())
            .then((json) => {
                this.setState({
                    user: json[0],
                });
            });
    }

    onCreate = (post) => {
        this.setState({
            postList: [post, ...this.state.postList],
        });
    };

    onMenuSelect = (currentMenu) => {
        this.setState({
            currentPageName: currentMenu,
        });
    };

    render() {
        let page = null;
        switch (this.state.currentPageName) {
            case 'news': page = <PostListLayoutComponent />;
                break;
            case 'mypage': console.log('mypage');
                break;
            default:
                page = <PostListLayoutComponent />;
        }

        return (
            <div>
                <NavbarTop user={this.state.user} />
                <Grid fluid>
                    <NavbarLeft onSelect={this.onMenuSelect}/>
                    <Col xs={12} md={8}>
                        { page }
                    </Col>
                </Grid>
            </div>
        );
    }
}

LayoutComponent.propTypes = {
    onSelect: React.PropTypes.func.isRequired,
};

export default LayoutComponent;
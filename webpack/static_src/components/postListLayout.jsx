import React, { Component } from 'react';
import PostFormComponent from './postForm';
import PostListComponent from './postList';
import PostComponent from './post';

export default class PostListLayoutComponent extends Component {
    state = {
        user: {
            id: 0,
            username: '',
        },
        postList: [],
        isLoading: true,
    };

    onCreate = (post) => {
        const postComponent =
            <PostComponent
                user={this.state.user}
                text={post.text}
                date={post.date}
            />;
        this.setState({
            postList: [postComponent, ...this.state.postList],
        });
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

        fetch('http://localhost:8000/api/v1/feed/?format=json',
            {
                method: 'GET',
                credentials: 'same-origin',
            })
            .then(promise => promise.json())
            .then((json) => {
                const list = json.map(
                    post => <PostComponent
                        key={post.id}
                        author={post.author.username}
                        text={post.text}
                        date={post.created_at}
                    />,
                );
                this.setState({
                    postList: list,
                    isLoading: false,
                });
            });
    }

    render() {
        return (
            <div>
                <PostFormComponent
                    onCreate={this.onCreate}
                    user={this.state.user}
                />
                <PostListComponent
                    postList={this.state.postList}
                    isLoading={this.state.isLoading}
                />
            </div>
        );
    }
}
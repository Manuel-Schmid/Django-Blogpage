export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = {
  [K in keyof T]: T[K];
};
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & {
  [SubKey in K]?: Maybe<T[SubKey]>;
};
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & {
  [SubKey in K]: Maybe<T[SubKey]>;
};
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  DateTime: any;
  GenericScalar: any;
  GraphqlError: any;
  Upload: any;
};

export type Category = {
  __typename?: "Category";
  id: Scalars["ID"];
  name: Scalars["String"];
  slug: Scalars["String"];
};

export type CategoryInput = {
  id?: InputMaybe<Scalars["ID"]>;
  name?: InputMaybe<Scalars["String"]>;
  slug?: InputMaybe<Scalars["String"]>;
};

export type Comment = {
  __typename?: "Comment";
  id: Scalars["ID"];
  owner: User;
  post: Post;
  text: Scalars["String"];
  title: Scalars["String"];
};

export type CommentInput = {
  id?: InputMaybe<Scalars["ID"]>;
  owner?: InputMaybe<Scalars["ID"]>;
  post?: InputMaybe<Scalars["ID"]>;
  text?: InputMaybe<Scalars["String"]>;
  title?: InputMaybe<Scalars["String"]>;
};

export type CreateCategory = {
  __typename?: "CreateCategory";
  category?: Maybe<Category>;
  errors?: Maybe<Scalars["GraphqlError"]>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type CreateComment = {
  __typename?: "CreateComment";
  comment?: Maybe<Comment>;
  errors?: Maybe<Scalars["GraphqlError"]>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type CreatePost = {
  __typename?: "CreatePost";
  errors?: Maybe<Scalars["GraphqlError"]>;
  post?: Maybe<Post>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type CreatePostLike = {
  __typename?: "CreatePostLike";
  errors?: Maybe<Scalars["GraphqlError"]>;
  postLike?: Maybe<PostLike>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type DeletePostLike = {
  __typename?: "DeletePostLike";
  errors?: Maybe<Scalars["GraphqlError"]>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type Mutation = {
  __typename?: "Mutation";
  createCategory?: Maybe<CreateCategory>;
  createComment?: Maybe<CreateComment>;
  createPost?: Maybe<CreatePost>;
  createPostLike?: Maybe<CreatePostLike>;
  deletePostLike?: Maybe<DeletePostLike>;
  refreshToken?: Maybe<Refresh>;
  testMutation?: Maybe<UploadMutation>;
  /** Obtain JSON Web Token mutation */
  tokenAuth?: Maybe<ObtainJsonWebToken>;
  updateCategory?: Maybe<UpdateCategory>;
  updateComment?: Maybe<UpdateComment>;
  updatePost?: Maybe<UpdatePost>;
  verifyToken?: Maybe<Verify>;
};

export type MutationCreateCategoryArgs = {
  categoryInput: CategoryInput;
};

export type MutationCreateCommentArgs = {
  commentInput: CommentInput;
};

export type MutationCreatePostArgs = {
  postInput: PostInput;
};

export type MutationCreatePostLikeArgs = {
  postId: Scalars["ID"];
};

export type MutationDeletePostLikeArgs = {
  postId: Scalars["ID"];
};

export type MutationRefreshTokenArgs = {
  refreshToken?: InputMaybe<Scalars["String"]>;
};

export type MutationTestMutationArgs = {
  fileInput: Scalars["Upload"];
};

export type MutationTokenAuthArgs = {
  password: Scalars["String"];
  username: Scalars["String"];
};

export type MutationUpdateCategoryArgs = {
  categoryInput: CategoryInput;
};

export type MutationUpdateCommentArgs = {
  commentInput: CommentInput;
};

export type MutationUpdatePostArgs = {
  postInput: PostInput;
};

export type MutationVerifyTokenArgs = {
  token?: InputMaybe<Scalars["String"]>;
};

/** Obtain JSON Web Token mutation */
export type ObtainJsonWebToken = {
  __typename?: "ObtainJSONWebToken";
  payload: Scalars["GenericScalar"];
  refreshExpiresIn: Scalars["Int"];
  refreshToken: Scalars["String"];
  token: Scalars["String"];
};

export type Post = {
  __typename?: "Post";
  category: Category;
  comments: Array<Comment>;
  dateCreated: Scalars["DateTime"];
  id: Scalars["ID"];
  image?: Maybe<Scalars["String"]>;
  isLiked?: Maybe<Scalars["Boolean"]>;
  likeCount?: Maybe<Scalars["Int"]>;
  owner: User;
  postLikes: Array<PostLike>;
  slug: Scalars["String"];
  tags?: Maybe<Array<Maybe<Tag>>>;
  text: Scalars["String"];
  title: Scalars["String"];
};

export type PostInput = {
  category?: InputMaybe<Scalars["ID"]>;
  owner?: InputMaybe<Scalars["ID"]>;
  slug?: InputMaybe<Scalars["String"]>;
  text?: InputMaybe<Scalars["String"]>;
  title?: InputMaybe<Scalars["String"]>;
};

export type PostLike = {
  __typename?: "PostLike";
  id: Scalars["ID"];
  post: Post;
  user: User;
};

export type Query = {
  __typename?: "Query";
  categories?: Maybe<Array<Maybe<Category>>>;
  categoryById?: Maybe<Category>;
  postBySlug?: Maybe<Post>;
  postLike?: Maybe<PostLike>;
  posts?: Maybe<Array<Maybe<Post>>>;
  tags?: Maybe<Array<Maybe<Tag>>>;
  usedTags?: Maybe<Array<Maybe<Tag>>>;
  user?: Maybe<User>;
  users?: Maybe<Array<Maybe<User>>>;
};

export type QueryCategoryByIdArgs = {
  id?: InputMaybe<Scalars["ID"]>;
};

export type QueryPostBySlugArgs = {
  slug?: InputMaybe<Scalars["String"]>;
};

export type QueryPostLikeArgs = {
  postId?: InputMaybe<Scalars["ID"]>;
};

export type QueryPostsArgs = {
  categorySlug?: InputMaybe<Scalars["String"]>;
  tagSlug?: InputMaybe<Scalars["String"]>;
};

export type Refresh = {
  __typename?: "Refresh";
  payload: Scalars["GenericScalar"];
  refreshExpiresIn: Scalars["Int"];
  refreshToken: Scalars["String"];
  token: Scalars["String"];
};

export type Tag = {
  __typename?: "Tag";
  name: Scalars["String"];
  slug: Scalars["String"];
};

export type UpdateCategory = {
  __typename?: "UpdateCategory";
  category?: Maybe<Category>;
  errors?: Maybe<Scalars["GraphqlError"]>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type UpdateComment = {
  __typename?: "UpdateComment";
  comment?: Maybe<Comment>;
  errors?: Maybe<Scalars["GraphqlError"]>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type UpdatePost = {
  __typename?: "UpdatePost";
  errors?: Maybe<Scalars["GraphqlError"]>;
  post?: Maybe<Post>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type UploadMutation = {
  __typename?: "UploadMutation";
  errors?: Maybe<Scalars["GraphqlError"]>;
  success?: Maybe<Scalars["Boolean"]>;
};

export type User = {
  __typename?: "User";
  email: Scalars["String"];
  firstName: Scalars["String"];
  id: Scalars["ID"];
  lastName: Scalars["String"];
  password: Scalars["String"];
  posts: Array<Post>;
  /** Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. */
  username: Scalars["String"];
};

export type Verify = {
  __typename?: "Verify";
  payload: Scalars["GenericScalar"];
};

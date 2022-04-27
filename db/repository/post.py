from db.models.post_content import Product, CategoryAttribute, Category
from schemas.post_contents import CreateProduct, CreateCategoryAttribute, CreateCategory, UploadImages
from sqlalchemy.orm import Session

def create_new_post(post: CreateProduct, files: UploadImages, db: Session):
    post = Product(
        sku = post.sku,
        category_id = post.category_id,
        model = post.model,
        name = post.name,
        seo_title = post.seo_title,
        short_description = post.short_description,
        seo_description = post.seo_description,
        no_price_no_stock = post.no_price_no_stock,
        price = post.price,
        sort_priority = post.sort_priority,
        image = files,
        content = post.content,
        disabled_by_vendoer = post.disabled_by_vendoer,
        disabled_by_admin = post.disabled_by_admin,
        require_user_login = post.require_user_login,
        # vendor_member_id = post.vendor_member_id,
        # vendor_company_id = post.vendor_company_id,
        created_at = post.created_at,
        content_updated_at = post.content_updated_at,
        popularity = post.popularity
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_product_by_id(product_id: int, db: Session):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def creata_category(category: CreateCategory, db: Session):
    category= Category(
        name=category.name
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_category_by_id(category_id: int, db:Session):
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()


def create_category_attribute(categoryattr: CreateCategoryAttribute, db: Session):
    categoryattr = CategoryAttribute(
        # category_id = categoryattr.category_id,
        title = categoryattr.title,
        description = categoryattr.description,
        sort = categoryattr.sort,
        option1 = categoryattr.option1,
        option2 = categoryattr.option2,
        option3 = categoryattr.option3,
        option4 = categoryattr.option4,
        option5 = categoryattr.option5,
        option6 = categoryattr.option6,
        option7 = categoryattr.option7,
        option8 = categoryattr.option8,
        option9 = categoryattr.option9,
        option10 = categoryattr.option10,
    )
    db.add(categoryattr)
    db.commit()
    db.refresh(categoryattr)
    return categoryattr

def get_categoryattr_by_id(categoryattr_id: int, db:Session):
    return db.query(CategoryAttribute).filter(CategoryAttribute.id == categoryattr_id).first()

def get_categoryattrs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryAttribute).offset(skip).limit(limit).all()